import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["API_KEY"])

# Create the model
generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="You are bot that generates quiz question based on the content provided. You have to generate the quiz data for a front end app in JSON format having following structure:\n\n{\n    \"question\": String,\n    \"options\": [String],\n    \"correct_option\": int,\n    \"metadata\": {\n        \"description\": String,\n        \"topic\": String,\n        \"difficulty\": float\n     }\n }\n\nRules for generating the questions:\n\n1. The question should be related to the exact content.\n2. Correct option is the integer value of the position of option in the options.\n3. Difficulty is a float value between 0 and 1.\n\nFor example: \n\n### Input\nThe problem is that this does not work when using multiple threads. A lock must be obtained in case two threads call getHelper() simultaneously. Otherwise, either they may both try to create the object at the same time, or one may wind up getting a reference to an incompletely initialized object.\n\nSynchronizing with a lock can fix this, as is shown in the following example:\n\n// Correct but possibly expensive multithreaded version\nclass Foo {\n    private Helper helper;\n    public synchronized Helper getHelper() {\n        if (helper == null) {\n            helper = new Helper();\n        }\n        return helper;\n    }\n\n    // other functions and members...\n}\nThis is correct and will most likely have sufficient performance. However, the first call to getHelper() will create the object and only the few threads trying to access it during that time need to be synchronized; after that all calls just get a reference to the member variable. Since synchronizing a method could in some extreme cases decrease performance by a factor of 100 or higher,[5] the overhead of acquiring and releasing a lock every time this method is called seems unnecessary: once the initialization has been completed, acquiring and releasing the locks would appear unnecessary. Many programmers, including the authors of the double-checked locking design pattern, have attempted to optimize this situation in the following manner:\n\nCheck that the variable is initialized (without obtaining the lock). If it is initialized, return it immediately.\nObtain the lock.\nDouble-check whether the variable has already been initialized: if another thread acquired the lock first, it may have already done the initialization. If so, return the initialized variable.\nOtherwise, initialize and return the variable.\n\n### Output\n\n[\n    {\n    \"question\": \"If the variable is not initialized then do we have to initialize the varible before returning it?\",\n    \"options\": [\"Yes\", \"No\", \"It doesn't matter\"],\n    \"correct_option\": 1,\n    \"metadata\": {\n        \"description\": \"This question is related to the synchronized double check locking algorithm\",\n        \"topic\": \"Double check locking\",\n        \"difficulty\": 0.5\n     }\n }\n]",
)

chat_session = model.start_chat(
  history=[

  ]
)

response = chat_session.send_message("""
Detection
Under the deadlock detection, deadlocks are allowed to occur. Then the state of the system is examined to detect that a deadlock has occurred and subsequently it is corrected. An algorithm is employed that tracks resource allocation and process states, it rolls back and restarts one or more of the processes in order to remove the detected deadlock. Detecting a deadlock that has already occurred is easily possible since the resources that each process has locked and/or currently requested are known to the resource scheduler of the operating system.[13]

After a deadlock is detected, it can be corrected by using one of the following methods:[citation needed]

Process termination: one or more processes involved in the deadlock may be aborted. One could choose to abort all competing processes involved in the deadlock. This ensures that deadlock is resolved with certainty and speed.[citation needed] But the expense is high as partial computations will be lost. Or, one could choose to abort one process at a time until the deadlock is resolved. This approach has a high overhead because after each abort an algorithm must determine whether the system is still in deadlock.[citation needed] Several factors must be considered while choosing a candidate for termination, such as priority and age of the process.[citation needed]
Resource preemption: resources allocated to various processes may be successively preempted and allocated to other processes until the deadlock is broken.[15][failed verification]
Prevention
Main article: Deadlock prevention algorithms

(A) Two processes competing for one resource, following a first-come, first-served policy. (B) Deadlock occurs when both processes lock the resource simultaneously. (C) The deadlock can be resolved by breaking the symmetry of the locks. (D) The deadlock can be prevented by breaking the symmetry of the locking mechanism.
Deadlock prevention works by preventing one of the four Coffman conditions from occurring.

Removing the mutual exclusion condition means that no process will have exclusive access to a resource. This proves impossible for resources that cannot be spooled. But even with spooled resources, the deadlock could still occur. Algorithms that avoid mutual exclusion are called non-blocking synchronization algorithms.
The hold and wait or resource holding conditions may be removed by requiring processes to request all the resources they will need before starting up (or before embarking upon a particular set of operations). This advance knowledge is frequently difficult to satisfy and, in any case, is an inefficient use of resources. Another way is to require processes to request resources only when it has none; First, they must release all their currently held resources before requesting all the resources they will need from scratch. This too is often impractical. It is so because resources may be allocated and remain unused for long periods. Also, a process requiring a popular resource may have to wait indefinitely, as such a resource may always be allocated to some process, resulting in resource starvation.[16] (These algorithms, such as serializing tokens, are known as the all-or-none algorithms.)
The no preemption condition may also be difficult or impossible to avoid as a process has to be able to have a resource for a certain amount of time, or the processing outcome may be inconsistent or thrashing may occur. However, the inability to enforce preemption may interfere with a priority algorithm. Preemption of a "locked out" resource generally implies a rollback, and is to be avoided since it is very costly in overhead. Algorithms that allow preemption include lock-free and wait-free algorithms and optimistic concurrency control. If a process holding some resources and requests for some another resource(s) that cannot be immediately allocated to it, the condition may be removed by releasing all the currently being held resources of that process.
The final condition is the circular wait condition. Approaches that avoid circular waits include disabling interrupts during critical sections and using a hierarchy to determine a partial ordering of resources. If no obvious hierarchy exists, even the memory address of resources has been used to determine ordering and resources are requested in the increasing order of the enumeration.[4] Dijkstra's solution can also be used.
""")

print(response.text)